# Higher-or-Lower-Game-Python1

This game is called Higher or Lower

Game Instructions:
  1. In this game, you'll compare two Instagram profiles.
  2. Your task is to guess which profile has more followers.
  3. If you guess correctly, you'll earn a point and move to the next round.
  4. The game keeps going until you make a wrong guess.

How I Created the Game:
  - I imported the right applications and files for the game.
  - I created a variable and started with a score of 0 points by default.
  - I used a flag named "game_over" that starts as False. This flag decides if the game should keep running using a repeating process called a while loop.
  - Inside the while loop, I made two variables called account_a and account_b that generate random Instagram profiles.
  - I checked if account A is the same as account B. If they are, I generated new ones.
  - I made a function that takes a profile and organizes its information.
  - Inside this function, I got the profile's name, description, country, and follower count and saved them separately to each variable.
  - To begin the game, I showed a special logo using ASCII characters.
  - Then I displayed the first Instagram profile.
  - After that, I used more ASCII characters to show a "VS" logo.
  - I showed the second Instagram profile.
  - I asked the player for their guess using an input function.
  - I checked if the answer was right by comparing follower counts using if statements.
  - If the player was right, player gets 1 point and and the game loops through.
  - If the player commits a mistake, the game ends. then the game logo and player score is displayed.
