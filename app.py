```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QAMAR KAIF</title>

    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #0f172a, #1e3a8a);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
        }

        .container {
            width: 90%;
            max-width: 650px;
            background: rgba(255, 255, 255, 0.10);
            padding: 40px;
            border-radius: 20px;
            text-align: center;
            box-shadow: 0 10px 35px rgba(0, 0, 0, 0.35);
            backdrop-filter: blur(10px);
        }

        h1 {
            font-size: 42px;
            letter-spacing: 3px;
            margin-bottom: 10px;
        }

        .subtitle {
            color: #cbd5e1;
            margin-bottom: 30px;
            font-size: 16px;
        }

        form {
            display: flex;
            gap: 10px;
            margin-bottom: 30px;
        }

        input {
            flex: 1;
            padding: 14px;
            border: none;
            border-radius: 10px;
            outline: none;
            font-size: 15px;
        }

        button {
            padding: 14px 22px;
            border: none;
            border-radius: 10px;
            background: #38bdf8;
            color: #0f172a;
            font-weight: bold;
            cursor: pointer;
        }

        button:hover {
            background: #7dd3fc;
        }

        h2 {
            margin-bottom: 15px;
            font-size: 22px;
        }

        ul {
            list-style: none;
        }

        li {
            background: rgba(255, 255, 255, 0.12);
            margin: 8px 0;
            padding: 12px;
            border-radius: 8px;
            text-align: left;
        }

        .footer {
            margin-top: 25px;
            font-size: 13px;
            color: #94a3b8;
        }
    </style>
</head>

<body>

    <div class="container">

        <h1>QAMAR KAIF</h1>

        <p class="subtitle">
            Welcome to my Flask Application
        </p>

        <form action="/submit" method="POST">
            <input
                type="text"
                name="new_message"
                placeholder="Enter your message..."
                required
            >

            <button type="submit">Submit</button>
        </form>

        <h2>Messages</h2>

        <ul>
            {% for message in messages %}
                <li>{{ message[0] }}</li>
            {% else %}
                <li>No messages yet.</li>
            {% endfor %}
        </ul>

        <div class="footer">
            Flask + MySQL Application
        </div>

    </div>

</body>
</html>
```
