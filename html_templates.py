css = '''
<style>
body {
    background-color: #1e1e1e;
}

/* WhatsApp-style background */
.main-container {
    background-image: url('https://i.pinimg.com/originals/77/da/28/77da28f61ae0b49c9e67c9e13c820f82.png');
    background-repeat: no-repeat;
    background-size: cover;
    height: 100vh;
    width: 100%;
}

/* Chat bubble styles */
.chat-message {
    padding: 0.8rem;
    border-radius: 10px;
    margin-bottom: 1rem;
    max-width: 70%;
    display: flex;
    align-items: center;
    word-wrap: break-word;
    font-family: 'Helvetica', sans-serif;
}

/* Green bubble for user messages */
.chat-message.user {
    background-color: #005c4b;
    align-self: flex-end;
    margin-left: auto;
    color: white;
}

/* Gray bubble for bot messages */
.chat-message.bot {
    background-color: #202c33;
    align-self: flex-start;
    margin-right: auto;
    border: 1px solid #333;
    color: white;
}

/* Avatar styling */
.chat-message .avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    margin-right: 10px;
}

.chat-message .avatar img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 50%;
}

/* Message content styling */
.chat-message .message {
    max-width: 80%;
    font-size: 0.9rem;
    line-height: 1.4;
    color: #e9edef;
}

/* Input text box with WhatsApp-like border and padding */
.stTextInput > div > input {
    background-color: #2a3942;
    color: white;
    padding: 12px;
    border: 1px solid #333;
    border-radius: 20px;
    font-size: 0.9rem;
    width: 100%;
}

/* Process button styling to resemble WhatsApp buttons */
.stButton button {
    background-color: #128c7e;
    color: white;
    padding: 10px;
    font-size: 1rem;
    border-radius: 5px;
    border: none;
    cursor: pointer;
}

.stButton button:hover {
    background-color: #075e54;
}

/* Spinner style with WhatsApp green */
.stSpinner {
    color: #25D366;
}

/* Time and Date Divider */
.date-divider {
    text-align: center;
    margin: 15px 0;
    font-size: 0.8rem;
    color: #919191;
    background-color: #111b21;
    padding: 5px;
    border-radius: 10px;
    display: inline-block;
}

.timestamp {
    font-size: 0.8rem;
    color: #818181;
    padding-left: 10px;
    float: right;
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://media.licdn.com/dms/image/v2/D4D03AQFyfa0EUWS6pg/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1715522597740?e=1731542400&v=beta&t=2S2HLzIzWQgK4jE8XQYG8tec5IV0t4zicyQGF1KFeHA" alt="Bot Avatar">
    </div>
    <div class="message">{{MSG}}<span class="timestamp"> {{TIME}}</span></div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/rdZC7LZ/Photo-logo-1.png" alt="User Avatar">
    </div>    
    <div class="message">{{MSG}}<span class="timestamp"> {{TIME}}</span></div>
</div>
'''
