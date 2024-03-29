<h1>Hello guys this is my First BIG PROJECT</h1>

Its typically a website which allow users to participate in a group and can discuss with other memebers about there problems.
Also user can create there own Rooms with Topic name - on which Group is based, Room name and Room Description.

Checkout my website at: http://harshRaj710.pythonanywhere.com

Follow me on LinkedIn: [https://linkedin.com/comm/mynetwork/discovery-see-all?usecase=PEOPLE_FOLLOWS&followMember=harsh-sahu-6957642a1](https://www.linkedin.com/in/harsh-sahu-6957642a1?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)

    - Create Rooms For Different Topics
    - Send Messages to Different rooms
    - Login/Signup via Google/Github Account
    - User can search Rooms through 
        - Creater Name
        - Room Name
        - Room Topic
        - Room Description

    
    To View Anyuser's Profile you need to Login First
        - Only then you can see other's Profile
        - Can send Messages to Rooms
        - Can create Room


    After Login And Creating Room User can Edit Room's Details,Delete Room


    User can Delete their Recent Activity 
        - Created Room
        - Send Messages
        via Recent Activity Tab


    Most Recent Activity will appear on the Top

    When a user tagged you in any group message, you will get notified via notification.
    
    Information within notification.
        - Message with username who tagged you and room name in which you tagged.
        - Room link to see message in which you tagged in.

------------------------------------------------------------------------------------------------------------------

<h1>All Methods/Notes are written on files</h1>

<h2>I followed DENIS IVY tutorial to create this Project but in many places i used my own methods + notification logic is developed by me.</h2>

I hope this Project will Help you in your Learning Journey...

Happy Coding

And Please forgive me if you found any Grammatical Mistake in my English. 


------------------------------------------------------------------------------------------------------------------


<h2>Major Problems Encountered while Doing this Project</h2>

**First**: Custom User Model Implementation
- Initially, I observed that Dennis Ivy implemented a Custom User Model using `AbstractUser`.
- However, I opted to create an additional model named `UserProfile` to incorporate features like bio and profile picture functionality. This model establishes a one-to-one relationship with the user model.

**Second**: Handling Signups via Google/Github
- An issue arose when users signed up via Google/Github, as their `UserProfile` was not populated, causing errors.
- To address this, I leveraged Django's signal features. Now, whenever a user signs up through Google/Github, a new object is created in the `UserProfile` model automatically.

**Third**: Managing the One-to-One Relationship
- Another challenge I encountered was managing the one-to-one relationship between the user and `UserProfile` models.
- To ensure seamless integration, I ensured that when a user signs up, their data is appropriately related to the `UserProfile`.


-----------------------------------------------------------------------------------------------------------------------

<h3>Problems</h3>

- As in this project, i not used django Channels so you need to manually update the website to see new messages.
- Try to show with-dot.png when new notification arrived for a user, and when user render notification file notification icon get changed with without-dot.png file

