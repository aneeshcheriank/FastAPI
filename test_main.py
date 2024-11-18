import pytest
from main import add

test_data = [(1, 2, 3), (-1, 3, 2), (-1, -1, -2), (0, 0, 0)]


# parameterize the test
@pytest.mark.parametrize("x,y,expected", test_data)
@pytest.mark.asyncio
async def test_add(x, y, expected):
    # force the fucntion to return since add is an asynchronous function
    value = await add(x, y)
    assert value["total"] == expected
