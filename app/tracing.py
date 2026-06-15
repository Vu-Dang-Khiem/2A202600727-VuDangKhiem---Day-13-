from __future__ import annotations

import os
from typing import Any

try:
    from langfuse import observe, get_client

    class _LangfuseContextAdapter:
        """Adapter bridging old langfuse_context API to langfuse v3 client."""
        def update_current_trace(self, **kwargs: Any) -> None:
            get_client().update_current_trace(**kwargs)

        def update_current_observation(self, **kwargs: Any) -> None:
            get_client().update_current_generation(**kwargs)

    langfuse_context = _LangfuseContextAdapter()

except Exception:
    def observe(*args: Any, **kwargs: Any):
        def decorator(func):
            return func
        return decorator

    class _DummyContext:
        def update_current_trace(self, **kwargs: Any) -> None:
            return None

        def update_current_observation(self, **kwargs: Any) -> None:
            return None

    langfuse_context = _DummyContext()


def tracing_enabled() -> bool:
    return bool(os.getenv("LANGFUSE_PUBLIC_KEY") and os.getenv("LANGFUSE_SECRET_KEY"))


def get_langfuse_client():
    if not tracing_enabled():
        return None
    try:
        from langfuse import get_client
        return get_client()
    except Exception:
        return None
