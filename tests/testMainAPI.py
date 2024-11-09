import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestMainAPI(unittest.TestCase):

    def test_read_root(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Welcome to the Receipt Processing API!"})

    def test_read_item(self):
        receipt = {
            "retailer": "Test Retailer",
            "purchaseDate": "2022-01-01",
            "purchaseTime": "12:00",
            "items": [
                {"shortDescription": "Item 1", "price": 10.0},
                {"shortDescription": "Item 2", "price": 20.0}
            ],
            "total": 30.0
        }
        response = client.post("/receipts/process", json=receipt)
        self.assertEqual(response.status_code, 200)
        receipt_id = response.json()["id"]

        response = client.get(f"/receipts/{receipt_id}/points")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_read_item_not_found(self):
        response = client.get("/receipts/invalid-id/points")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"detail": "No receipt found for that id"})

    def test_process_receipt_1(self):
        receipt = {
            "retailer": "Test Retailer",
            "purchaseDate": "2022-01-01",
            "purchaseTime": "12:00",
            "items": [
                {"shortDescription": "Item 1", "price": 10.0},
                {"shortDescription": "Item 2", "price": 20.0}
            ],
            "total": 30.0
        }
        response = client.post("/receipts/process", json=receipt)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        self.assertIn("id", response.json())

        receipt_id = response.json()["id"]
        response = client.get(f"/receipts/{receipt_id}/points")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        points = response.json().get("points")
        self.assertEqual(points, 104)

    def test_process_receipt_2(self):
        receipt = {
            "retailer": "Target",
            "purchaseDate": "2022-01-01",
            "purchaseTime": "13:01",
            "items": [
                {
                "shortDescription": "Mountain Dew 12PK",
                "price": "6.49"
                },{
                "shortDescription": "Emils Cheese Pizza",
                "price": "12.25"
                },{
                "shortDescription": "Knorr Creamy Chicken",
                "price": "1.26"
                },{
                "shortDescription": "Doritos Nacho Cheese",
                "price": "3.35"
                },{
                "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
                "price": "12.00"
                }
            ],
            "total": "35.35"
        }
        response = client.post("/receipts/process", json=receipt)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        self.assertIn("id", response.json())

        receipt_id = response.json()["id"]
        response = client.get(f"/receipts/{receipt_id}/points")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        points = response.json().get("points")
        self.assertEqual(points, 28)


    def test_process_receipt_2(self):
        receipt = {
            "retailer": "M&M Corner Market",
            "purchaseDate": "2022-03-20",
            "purchaseTime": "14:33",
            "items": [
                {
                "shortDescription": "Gatorade",
                "price": "2.25"
                },{
                "shortDescription": "Gatorade",
                "price": "2.25"
                },{
                "shortDescription": "Gatorade",
                "price": "2.25"
                },{
                "shortDescription": "Gatorade",
                "price": "2.25"
                }
            ],
            "total": "9.00"
        }
        response = client.post("/receipts/process", json=receipt)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        self.assertIn("id", response.json())

        receipt_id = response.json()["id"]
        response = client.get(f"/receipts/{receipt_id}/points")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        points = response.json().get("points")
        self.assertEqual(points, 109)

    def test_process_receipt_invalid_request(self):
        receipt = {
            "invalid_key": "Test Retailer"
        }
        response = client.post("/receipts/process", json=receipt)
        self.assertEqual(response.status_code, 422)




if __name__ == "__main__":
    unittest.main()