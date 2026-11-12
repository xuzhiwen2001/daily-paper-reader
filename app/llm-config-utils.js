(function (root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) {
    module.exports = api;
  }
  if (root) {
    root.DPRLLMConfigUtils = api;
  }
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  const DEFAULT_DEEPSEEK_BASE_URL = 'https://api.deepseek.com';
  const DEFAULT_DEEPSEEK_CHAT_MODELS = [
    'deepseek-v4-flash',
    'deepseek-v4-pro',
  ];
  const DEEPSEEK_V4_MAX_OUTPUT_TOKENS = 393216;
  const DEEPSEEK_PRESETS = Object.freeze({
    deepseek: Object.freeze({
      key: 'deepseek',
      label: 'DeepSeek 官方',
      baseUrl: 'https://api.deepseek.com',
      models: Object.freeze(['deepseek-v4-flash', 'deepseek-v4-pro']),
    }),
  });
  // 多厂商预设：所有端点均需兼容 OpenAI chat/completions 协议。
  // coding 套餐按“每 5 小时 N 次 prompts”计额，适合低频任务；高频批量建议用按量端点。
  const LLM_PROVIDER_PRESETS = Object.freeze({
    deepseek: Object.freeze({
      key: 'deepseek',
      label: 'DeepSeek 官方（按量）',
      baseUrl: 'https://api.deepseek.com',
      models: Object.freeze(['deepseek-v4-flash', 'deepseek-v4-pro']),
      note: 'DeepSeek 官方 API，按量计费。',
    }),
    'glm-coding': Object.freeze({
      key: 'glm-coding',
      label: 'GLM Coding 套餐（智谱）',
      baseUrl: 'https://open.bigmodel.cn/api/coding/paas/v4',
      models: Object.freeze(['glm-4.6', 'glm-4.5']),
      note: '需要 GLM Coding 套餐 key（通用端点不认套餐 key）；按 5 小时窗口计额。浏览器测试可能因 CORS 限制失败（Failed to fetch），不影响在 GitHub Actions 中使用。',
    }),
    zhipu: Object.freeze({
      key: 'zhipu',
      label: '智谱开放平台（按量）',
      baseUrl: 'https://open.bigmodel.cn/api/paas/v4',
      models: Object.freeze(['glm-4.6', 'glm-4.5']),
      note: '智谱标准按量计费 API。浏览器测试可能因 CORS 限制失败，不影响 CI 使用。',
    }),
    moonshot: Object.freeze({
      key: 'moonshot',
      label: 'Kimi 开放平台（按量）',
      baseUrl: 'https://api.moonshot.cn/v1',
      models: Object.freeze(['kimi-k2-0905-preview', 'kimi-k2-turbo-preview']),
      note: 'Moonshot 标准按量计费 API（Kimi For Coding 套餐 key 与开放平台 key 不通用）。',
    }),
    siliconflow: Object.freeze({
      key: 'siliconflow',
      label: '硅基流动 SiliconFlow',
      baseUrl: 'https://api.siliconflow.cn/v1',
      models: Object.freeze(['deepseek-ai/DeepSeek-V3', 'Qwen/Qwen3-235B-A22B']),
      note: '模型聚合平台，按量计费。',
    }),
    custom: Object.freeze({
      key: 'custom',
      label: '自定义 OpenAI 兼容接口',
      baseUrl: '',
      models: Object.freeze([]),
      note: '填写任意兼容 OpenAI chat/completions 的端点（如自建 vLLM / Ollama / OpenRouter）。',
    }),
  });

  const normalizeText = (value) => String(value || '').trim();

  const normalizeBaseUrlForStorage = (value) => {
    let text = normalizeText(value).replace(/\/+$/g, '');
    if (!text) return '';
    text = text.replace(/\/chat\/completions$/i, '');
    return text.replace(/\/+$/g, '');
  };

  const buildChatCompletionsEndpoint = (value) => {
    const raw = normalizeText(value).replace(/\/+$/g, '');
    if (!raw) return '';
    if (/\/chat\/completions$/i.test(raw)) return raw;
    const normalized = normalizeBaseUrlForStorage(raw);
    if (!normalized) return '';
    if (/\/v\d+$/i.test(normalized)) {
      return `${normalized}/chat/completions`;
    }
    return `${normalized}/v1/chat/completions`;
  };

  const sanitizeModelList = (values, maxCount = 3) => {
    const rawList = Array.isArray(values) ? values : [values];
    const out = [];
    const seen = new Set();
    for (const value of rawList) {
      const parts = String(value || '')
        .split(/[\n,]+/)
        .map((item) => normalizeText(item))
        .filter(Boolean);
      for (const name of parts) {
        const key = name.toLowerCase();
        if (!key || seen.has(key)) continue;
        seen.add(key);
        out.push(name);
        if (out.length >= Math.max(Number(maxCount) || 0, 1)) {
          return out;
        }
      }
    }
    return out;
  };

  const resolveChatModels = (secret) => {
    const safeSecret = secret && typeof secret === 'object' ? secret : {};
    const chatList = Array.isArray(safeSecret.chatLLMs) ? safeSecret.chatLLMs : [];
    const models = [];
    const seen = new Set();
    chatList.forEach((item) => {
      if (!item || typeof item !== 'object') return;
      const baseUrl = normalizeBaseUrlForStorage(item.baseUrl || '');
      const apiKey = normalizeText(item.apiKey || '');
      const modelNames = sanitizeModelList(item.models || [], 99);
      if (!baseUrl || !apiKey || !modelNames.length) return;
      modelNames.forEach((name) => {
        const dedupeKey = `${name.toLowerCase()}\u0000${baseUrl}\u0000${apiKey}`;
        if (seen.has(dedupeKey)) return;
        seen.add(dedupeKey);
        models.push({
          name,
          apiKey,
          baseUrl,
        });
      });
    });
    return models;
  };

  const resolveSummaryLLM = (secret) => {
    const safeSecret = secret && typeof secret === 'object' ? secret : {};
    const summarized = safeSecret.summarizedLLM || {};
    const baseUrl = normalizeBaseUrlForStorage(summarized.baseUrl || '');
    const apiKey = normalizeText(summarized.apiKey || '');
    const model = normalizeText(summarized.model || '');
    if (baseUrl && apiKey && model) {
      return { baseUrl, apiKey, model };
    }

    const chatModels = resolveChatModels(safeSecret);
    if (!chatModels.length) return null;
    return {
      baseUrl: normalizeBaseUrlForStorage(chatModels[0].baseUrl || ''),
      apiKey: normalizeText(chatModels[0].apiKey || ''),
      model: normalizeText(chatModels[0].name || ''),
    };
  };

  const inferProviderType = (secret) => {
    const safeSecret = secret && typeof secret === 'object' ? secret : {};
    const llmProvider = safeSecret.llmProvider || {};
    const explicit = normalizeText(llmProvider.type || llmProvider.provider || '').toLowerCase();
    if (explicit && LLM_PROVIDER_PRESETS[explicit]) {
      return explicit;
    }
    return 'deepseek';
  };

  const getProviderPreset = (key) => {
    const presetKey = normalizeText(key).toLowerCase();
    const preset = LLM_PROVIDER_PRESETS[presetKey];
    if (!preset) return null;
    return {
      key: preset.key,
      label: preset.label,
      baseUrl: preset.baseUrl,
      models: [...preset.models],
      note: preset.note || '',
    };
  };

  const listProviderPresets = () => {
    return Object.keys(LLM_PROVIDER_PRESETS).map((key) => getProviderPreset(key));
  };

  // 兼容旧调用：等价于 getProviderPreset('deepseek')。
  const getDeepSeekPreset = (key) => {
    const presetKey = normalizeText(key).toLowerCase();
    if (presetKey && presetKey !== 'deepseek') {
      return getProviderPreset(presetKey);
    }
    return getProviderPreset('deepseek');
  };

  // 依据 base URL / 模型名推断厂商画像；未知主机一律视为通用
  // OpenAI 兼容端点（openai），只有完全为空才返回 unsupported。
  const inferChatApiProfile = (baseUrl, model) => {
    const normalizedBaseUrl = normalizeBaseUrlForStorage(baseUrl || '').toLowerCase();
    const normalizedModel = normalizeText(model || '').toLowerCase();
    if (/(^|\/\/)(api\.)?deepseek\.com(?:$|\/)/i.test(normalizedBaseUrl)) {
      return 'deepseek';
    }
    if (/(^|\/\/)open\.bigmodel\.cn(?:$|\/)/i.test(normalizedBaseUrl)) {
      return 'zhipu';
    }
    if (/(^|\/\/)(api\.)?kimi\.com(?:$|\/)|(^|\/\/)api\.moonshot\.cn(?:$|\/)/i.test(normalizedBaseUrl)) {
      return 'moonshot';
    }
    if (/(^|\/\/)api\.siliconflow\.cn(?:$|\/)/i.test(normalizedBaseUrl)) {
      return 'siliconflow';
    }
    if (!normalizedBaseUrl) {
      return normalizedModel.startsWith('deepseek-') ? 'deepseek' : 'unsupported';
    }
    return 'openai';
  };

  const resolveJsonResponseMode = ({ baseUrl, model, preferSchema = true }) => {
    return 'json_object';
  };

  const isDeepSeekV4Model = (model) => {
    const normalizedModel = normalizeText(model || '').toLowerCase();
    return normalizedModel === 'deepseek-v4-flash' || normalizedModel === 'deepseek-v4-pro';
  };

  const resolveMaxOutputTokens = ({ baseUrl, model } = {}) => {
    const profile = inferChatApiProfile(baseUrl, model);
    if (profile === 'deepseek' && isDeepSeekV4Model(model)) {
      return DEEPSEEK_V4_MAX_OUTPUT_TOKENS;
    }
    return null;
  };

  const shouldUseXApiKeyHeader = ({ baseUrl, model }) => {
    return true;
  };

  const buildStreamingChatPayload = ({ baseUrl, model, messages }) => {
    const payload = {
      model: normalizeText(model),
      messages: Array.isArray(messages) ? messages : [],
      stream: true,
    };
    const maxTokens = resolveMaxOutputTokens({ baseUrl, model });
    if (maxTokens) {
      payload.max_tokens = maxTokens;
    }
    return payload;
  };

  const buildConnectivityTestPayload = ({ baseUrl, model }) => {
    const normalizedModel = normalizeText(model);
    return {
      model: normalizedModel,
      messages: [
        {
          role: 'system',
          content: 'Reply with exactly: hello world',
        },
        {
          role: 'user',
          content: 'hello world',
        },
      ],
      temperature: 0,
      max_tokens: 256,
    };
  };

  return {
    DEFAULT_DEEPSEEK_BASE_URL,
    DEFAULT_DEEPSEEK_CHAT_MODELS,
    DEEPSEEK_PRESETS,
    LLM_PROVIDER_PRESETS,
    normalizeText,
    normalizeBaseUrlForStorage,
    buildChatCompletionsEndpoint,
    sanitizeModelList,
    resolveChatModels,
    resolveSummaryLLM,
    inferProviderType,
    getProviderPreset,
    listProviderPresets,
    getDeepSeekPreset,
    inferChatApiProfile,
    resolveJsonResponseMode,
    isDeepSeekV4Model,
    resolveMaxOutputTokens,
    shouldUseXApiKeyHeader,
    buildStreamingChatPayload,
    buildConnectivityTestPayload,
  };
});
