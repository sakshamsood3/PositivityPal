# PositivityPal

Positivity Pal, the amazing Discord bot that's here to lift you up when you're feeling down. With its collection of inspiring quotes from famous authors and personalities, this incredible bot becomes your personal cheerleader, always ready to encourage and motivate you.
Say goodbye to negativity as Positivity Pal guides you towards a brighter path, filling your heart with uplifting words of wisdom. Let this special companion be your source of comfort and inspiration!

Default command Character: $

Here is a list of functions and commands recognised by the bot to provide an array of functionalities:

1. $inspire -> The inspire command fetches and displays a Random quote from the internet that belongs
   to a well renowned person

2. Whenever the user types in a message,the bot will check the entire sentence against a list of words containing 1000+ negative words that might hint at the user being at distress, and it will display an encouraging message to motivate and cheer up the user

3. $new [quote] -> the new command allows users to enter a custom message used for encouragement which is added to the list of pre defined encouraging messages.
   For Example: $new You are the best

4. $del [index] -> the del command allows the user to delete the user defined encouraging messages present at a certain index.
   For Example: $del 1

5. $responding {true,false} -> The responding command is used to control the functionality of the bot.
   When it is set to true the bot feature of displaying a motivating/encouraging message to the User whenever they type in something which contains negative sentiment is turned on and stays on till it is explicitly turned off.
   When it is set to true the bot feature of displaying a motivating/encouraging message to the User whenever they type in something which contains negative sentiment is turned off and stays off till it is explicitly turned on.
   By default this feature is turned on.
