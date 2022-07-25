# vernamcipher-chatapp

vernamcipher-chatapp is a chat application made with DRF, Django-Channels and websockets.

## Installation

For now you can clone from the staging branch, but it will be merged with master soon.

```bash
git clone --branch staging https://github.com/cheezedoodles/vernamcipher-chatapp.git
```
## Database model

![Alt text](https://i.postimg.cc/wjzj3KcF/database.png?raw=true "Database image")
## Usage

Firstly, you'll need to make migrations:
```bash
python manage.py makemigrations
```
And then apply them to the database:
```bash
python manage.py migrate
```
After that feel free to run django and docker servers:
```bash
docker run -p 6379:6379 -d redis:5
```
```bash
python manage.py runserver
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)