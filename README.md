# Short links and clics count

Utility for shortening links and for information (clics count, expanded link) about shortened links using VK API.
### How to install
 
Python3 should already be installed. 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
If you load project locally, then create `.env` file in project directory.

In .env write and fill `VK_SERVICE_ACCESS_KEY`.

If you load project on service (like replit) then just add a secret key `VK_SERVICE_ACCESS_KEY` and fill it.

Api key can be obtained via [instruction](https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/tokens/service-token).

Example:
`VK_SERVICE_ACCESS_KEY = '65cc8c6765cc8c6765cc8c67e466d4ebb4665fe65cc8c6703qwea96d78517798bcde495'`
### How to use

#### Windows OS

Open cmd/powershell/etc.

Change current directory in console to project directory by cd command.

Run script by command:

`py main.py`

#### Linux OS

Open console.

Change current directory in console to project directory by cd command.

Run script by command:

`python3 main.py`

### Examples of running script

Running example

![Example3](https://github.com/e13q/WA_lesson2/assets/110967581/2c701e76-a78c-48b0-affd-d188f886bd5c)


Get shorten link

![Example](https://github.com/e13q/WA_lesson2/assets/110967581/f84f1393-5a76-4bff-aea4-8874e15572aa)

Get info about shorten link

![Example2](https://github.com/e13q/WA_lesson2/assets/110967581/f5069073-2032-4d2e-b30a-7268080ef557)

### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).
