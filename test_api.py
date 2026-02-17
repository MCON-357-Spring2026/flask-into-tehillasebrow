import requests
#Test the Welcome Route
def test_welcome():
    response = requests.get('http://localhost:5000/')
    print(f"Status Code: {response.status_code}")
    print(f"Content: {response.text}")
#Test the About Route
def test_about():
    response = requests.get('http://localhost:5000/about')
    print(f"Status Code: {response.status_code}")
    if response.status_code ==200:
        data = response.json()
        print("Name:", data.get("name"))
        print("Course:", data.get("course"))
        print("Semester:", data.get("semester"))

#Test the Greeting Route
def test_greeting():
    response = requests.get('http://localhost:5000/greet/Tehilla')
    print(f"Status Code: {response.status_code}")
    if "Tehilla" in response.text:
        print("Greeting contains name")
    else:
        print("Greeting does not contain name")
    print(f"Content: {response.text}")

#Test the Calculator Route
def test_calc():
    response=requests.get('http://localhost:5000/calculate?num1=10&num2=1&operation=multiply')
    print("Multiply Result:", response.json())
    response1=requests.get('http://localhost:5000/calculate?num1=10&num2=1&operation=add')
    print("Adding Result:", response1.json())
    response3=requests.get('http://localhost:5000/calculate?num1=10&num2=0&operation=divide')
    print("Divide by Zero Status:", response3.status_code)
    print("Dividing by Zero Result:", response3.json())
#Test the Echo Route (POST)
def test_echo():
    response = requests.post('http://localhost:5000/echo',json={"message": "Hello Flask"})
    print(f"Status Code: {response.status_code}")
    print(f"Content: {response.json()}")
    if response.json().get("echoed"):
        print("Echo confirmed")
    else:
        print("Echo failed")

#Test Different Status Codes
def test_status_codes():
    response = requests.get('http://localhost:5000/status/201')
    response1 = requests.get('http://localhost:5000/status/403')
    print(f"Status Code: {response.status_code}")
    print(f"Content: {response.text}")
    print(f"Status Code: {response1.status_code}")
    print(f"Content: {response1.text}")
#Test Custom Headers
def test_headers():
    response = requests.get('http://localhost:5000/')
    custom_header = response.headers.get('X-Custom-Header')
    print(f"Custom Header: {custom_header}")
    if custom_header == "FlaskRocks":
        print("Custom header verified")
    else:
        print("Custom header missing")

#Test Error Handling
def test_error_handling():
    response = requests.get('http://localhost:5000/calculate?num1=10&num2=0&operation=divide')
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    print("Starting API Tests...")

    test_welcome()
    test_about()
    test_greeting()
    test_calc()
    test_echo()
    test_status_codes()
    test_headers()
    test_error_handling()

    print("\nAll tests completed.")