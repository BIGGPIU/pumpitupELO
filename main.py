import requests
KEY = "710a11f3-2ec6-48eb-9d51-28116672d435"
sheaders = {
    'accept: */*'
    'Authorization: Basic VEhFUkVJU0FCT01CU1RSQVBQRURUT01ZQ0hFU1Q6NzEwYTExZjMtMmVjNi00OGViLTlkNTEtMjgxMTY2NzJkNDM1'
}
response = requests.get("https://piuscores.arroweclip.se/api/phoenixScores?Page=1&Count=50", headers={
    'accept':'*/*',
    'Authorization':'Basic VEhFUkVJU0FCT01CU1RSQVBQRURUT01ZQ0hFU1Q6NzEwYTExZjMtMmVjNi00OGViLTlkNTEtMjgxMTY2NzJkNDM1'
})
print (response.json())

