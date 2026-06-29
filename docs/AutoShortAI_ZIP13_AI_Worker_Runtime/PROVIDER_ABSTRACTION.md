# Provider Abstraction

Provider-specific code must live behind adapters.

The core sees:

- AIProvider
- AIProviderConfig
- AIProviderCapability
- AIProviderRequest
- AIProviderResponse
- AIProviderCost

Future providers can be added without changing the core runtime.
