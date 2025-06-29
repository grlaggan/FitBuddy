import jwt
from typing import Any
from src import sets

from datetime import datetime, timedelta, timezone


def encode(
    payload: dict,
    algorithm: str = sets.jwt.algorithm,
    private_key: str = sets.jwt.private_key,
    access_token_minutes_expire: int = sets.jwt.access_token_minutes_expire,
    refresh_token_days_expire: int | None = None,
) -> str:
    to_payload = payload.copy()

    now = datetime.now(tz=timezone.utc)
    if refresh_token_days_expire:
        to_payload.update(
            {
                "exp": now + timedelta(days=refresh_token_days_expire),
                "iat": now,
            }
        )
    else:
        to_payload.update(
            {
                "exp": now + timedelta(minutes=access_token_minutes_expire),
                "iat": now,
            }
        )

    token = jwt.encode(to_payload, private_key, algorithm=algorithm)
    return token


def decode(
    token: str,
    algorithm: str = sets.jwt.algorithm,
    public_key: str = sets.jwt.public_key,
) -> dict[str, Any]:
    payload = jwt.decode(token, public_key, algorithms=[algorithm])
    return payload
