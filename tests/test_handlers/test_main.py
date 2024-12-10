import pytest


@pytest.mark.asyncio
async def test_read_products(client):
    """Test endpoint for read all products"""
    response = client.get("/api/products/all")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_read_brands(client):
    """Test endpoint for read all brands"""
    response = client.get("/api/products/brands/all")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_admin_page(client):
    """Test endpoint for admin page"""
    response = client.get("/admin")
    assert response.status_code == 200

