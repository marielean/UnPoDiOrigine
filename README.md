# Un po' di origine - ECommerce
## Testing
The app is tested using the TestCase class of Django. In order to start tests
launch
```bash
python3 manage.py test
```
If you want to measure the test coverage you can launch
```bash
coverage run --source='.' manage.py test
```
The command executes tests and analyzes how much they cover the code. In order
to generate a report you can write
```bash
coverage report
```
or
```bash
coverage html
```
to visualize as html.