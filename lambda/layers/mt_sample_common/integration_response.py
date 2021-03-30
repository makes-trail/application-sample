import json


def map(status_code: int, body: str = None) -> dict:
    """Lambdaプロキシ統合の形式にマップする

    Parameters
    ----------
    statu_code: str
        ステータスコード
    body: str
        レスポンスボディ
    
    Returns
    -------
    response: dict
        Lambdaプロキシ統合形式のレスポンス
    """

    headers = {
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "*"
    }
    response = {
        "statusCode": status_code,
        "headers": headers
    }
    if body is not None:
        response["body"] = body
    
    return response
