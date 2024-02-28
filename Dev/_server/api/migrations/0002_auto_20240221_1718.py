# Generated by Django 5.0.2 on 2024-02-21 17:18
from datetime import datetime, timedelta

from django.db import migrations,transaction
from django.contrib.auth.hashers import make_password
from django.utils.timezone import make_aware


def dummy_dater1(User, Dater):
    """
    Create the first dummy dater.
    User: Model to use for User
    Dater: Model to use for Dater
    Returns: created dater
    """

    user = User(
        username = 'dater1',
        password = make_password('password'),
        email = 'bob@cupid_code.com',
        first_name = 'Bob',
        last_name = 'The Builder',
    )
    user.save()

    dater1 = Dater(
        user = user,
        phone_number = '1234567890',
        budget = 50,
        communication_preference = 0,
        description = 'I like to build things in my spare time.',
        dating_strengths = 'Building things is cool',
        dating_weaknesses = 'Not everyone likes to talk about building things all the time.',
        interests = 'Carpentry',
        past = "I've never dated in my whole life.",
        nerd_type = 'building',
        relationship_goals = 'Find the one',
        ai_degree = 'I need all the help',
        cupid_cash_balance = 200,
        location = 'Logan, UT',
        average_rating = 4.3,
        is_suspended = False,
    )

    #This portion should happen automatically, but that doesn't work in migrations
    dater1.user.role = "Dater"
    dater1.user.save()

    dater1.save()
    return dater1

def dummy_dater2(User, Dater):
    """
    Create the second dummy dater.
    User: Model to use for User
    Dater: Model to use for Dater
    Returns: created dater
    """
    
    user = User(
        username = 'dater2',
        password = make_password('password'),
        email = 'Manny@cupid_code.com',
        first_name = 'Handy',
        last_name = 'Manny',
    )
    user.save()

    dater2 = Dater(
        user = user,
        phone_number = '1223334444',
        budget = 50,
        communication_preference = 0,
        description = 'I fix things for people around town',
        dating_strengths = 'Helping people is cool',
        dating_weaknesses = 'I do not know how to do it',
        interests = 'Tools',
        past = "I have been on many dates and in a few relationships. They all ended poorly.",
        nerd_type = 'building',
        relationship_goals = 'Find a girlfriend and see how it goes',
        ai_degree = "I don't need your help",
        cupid_cash_balance = 20,
        location = 'Logan, UT',
        average_rating = 3.3,
        is_suspended = False,
    )

    #This portion should happen automatically, but that doesn't work in migrations
    dater2.user.role = "Dater"
    dater2.user.save()

    dater2.save()
    return dater2

def dummy_messages1(dater, Message):
    """
    Create a sample conversation.
    dater: The dater who owns the conversation.
    Message: Model to use for Message
    """

    message1 = Message(
        owner = dater,
        text = 'Hi AI, I need help.',
        from_ai = False
    )
    message2 = Message(
        owner = dater,
        text = 'No',
        from_ai = True
    )
    message3 = Message(
        owner = dater,
        text = 'Thanks for nothing',
        from_ai = False
    )

    message1.save()
    message2.save()
    message3.save()

def dummy_messages2(dater, Message):
    """
    Create a sample conversation.
    dater: The dater who owns the conversation.
    Message: Model to use for Message
    """

    message1 = Message(
        owner = dater,
        text = 'Good day robot. I would greatly appreciate your assistance in my date. What should I say next?',
        from_ai = False
    )
    message2 = Message(
        owner = dater,
        text = 'Ask them about themselves instead of talking about yourself.',
        from_ai = True
    )
    message3 = Message(
        owner = dater,
        text = 'Thank you for the help good sir.',
        from_ai = False
    )

    message1.save()
    message2.save()
    message3.save()

@transaction.atomic
def dummy_unclaimed(dater, Gig, Quest):
    """
    Create sample unclaimed gigs.
    dater: The dater who owns the gigs.
    Gig: Model to use for Gig
    Quest: Model to use for Quest
    Returns: tuple of created gigs
    """

    quest1 = Quest(
        budget = 20,
        items_requested = 'Flowers',
        pickup_location = 'Smiths'
    )
    quest2 = Quest(
        budget = 10,
        items_requested = 'Chocolate',
        pickup_location = 'Smiths'
    )

    quest1.save()
    quest2.save()

    gig1 = Gig(
        dater = dater,
        quest = quest1,
        status = 0,
        date_time_of_request = make_aware(datetime.now()),
    )

    gig2 = Gig(
        dater = dater,
        quest = quest2,
        status = 0,
        date_time_of_request = make_aware(datetime.now()),
    )

    gig1.save()
    gig2.save()

    return (gig1, gig2)

@transaction.atomic
def dummy_claimed(dater, cupid, Gig, Quest):
    """
    Create sample claimed gig.
    dater: The dater who owns the gigs.
    cupid: the cupid who claimed the gig.
    Gig: Model to use for Gig
    Quest: Model to use for Quest
    Returns: tuple of gig
    """

    quest = Quest(
        budget = 200,
        items_requested = 'Concert tickets',
        pickup_location = 'Not Smiths'
    )

    quest.save()

    gig = Gig(
        dater = dater,
        quest = quest,
        cupid = cupid,
        status = 1,
        date_time_of_request = make_aware(datetime.now() - timedelta(minutes=15)),
        date_time_of_claim = make_aware(datetime.now() - timedelta(minutes=5)),
    )

    gig.save()

    return (gig,)


def dummy_cupid1(User, Cupid):
    """
    Create the first sample cupid.
    User: The model to use for User
    Cupid: The model to use for Cupid
    Returns: The created cupid
    """

    user = User(
        username = 'cupid1',
        password = make_password('password'),
        email = 'joe@mail.com',
        first_name = 'Joe',
        last_name = 'Brown',
    )

    user.save()

    cupid1 = Cupid(
        user = user,
        accepting_gigs = False,
        gigs_completed = 54,
        gigs_failed = 11,
        status = 1,
        cupid_cash_balance = 1100,
        gig_range = 20,
        location = 'Logan, UT',
        average_rating = 4.1,
        is_suspended = False,
    )

    #This portion should happen automatically, but that doesn't work in migrations
    cupid1.user.role = "Cupid"
    cupid1.user.save()

    cupid1.save()

    return cupid1

def dummy_cupid2(User, Cupid):
    """
    Create the second sample cupid.
    User: The model to use for User
    Cupid: The model to use for Cupid
    Returns: The created cupid
    """

    user = User(
        username = 'cupid2',
        password = make_password('password'),
        email = 'really@me.com',
        first_name = 'Cupid',
        last_name = 'Himself',
    )

    user.save()

    cupid2 = Cupid(
        user = user,
        accepting_gigs = False,
        gigs_completed = 4,
        gigs_failed = 16,
        status = 0,
        cupid_cash_balance = 12,
        location = 'Logan, UT',
        gig_range = 20,
        average_rating = 1.2,
        is_suspended = False,
    )

    #This portion should happen automatically, but that doesn't work in migrations
    cupid2.user.role = "Cupid"
    cupid2.user.save()

    cupid2.save()

    return cupid2

def dummy_manager(User):
    """
    Create the sample manager.
    User: The model to use for User
    """

    user = User(
        username = 'manager',
        password = make_password('password'),
        email = 'manager@cupid_code.com',
        first_name = 'Mr.',
        last_name = 'Boss',
        is_staff = True,
        role = "Manager"
    )

    user.save()

def dummy_dates(dater1, dater2, Date):
    """
    Create the sample manager.
    User: The model to use for User
    """

    date1 = Date(
        dater = dater1,
        date_time = make_aware(datetime.now() + timedelta(days = 45)),
        location = 'McDonalds',
        description = 'Gonna get some chicken nuggets',
        status = 'planned',
        budget = 12.5,
    )

    date2 = Date(
        dater = dater1,
        date_time = make_aware(datetime.now() + timedelta(days = 40)),
        location = 'Wendys',
        description = 'I love me some chicken nuggets',
        status = 'planned',
        budget = 27.5,
    )

    date3 = Date(
        dater = dater2,
        date_time = make_aware(datetime.now() + timedelta(days = 48)),
        location = 'Park',
        description = 'Gonna go for a walk',
        status = 'planned',
        budget = 1.5,
    )

    date1.save()
    date2.save()
    date3.save()

def dummy_feedbacks(gigs, Feedback):
    """
    Create the sample feedbacks.
    gigs: list of gigs to use in creating feedback
    Feedback: The model to use for Feedback
    """

    gig0_dater = Feedback(
        user = gigs[0].dater.user,
        gig = gigs[0],
        message = 'I do not want to deliver to this guy',
        star_rating = 0,
        date_time = gigs[0].date_time_of_request
    )

    gig1_dater = Feedback(
        user = gigs[1].dater.user,
        gig = gigs[1],
        message = 'This guy is great, but I do not have time',
        star_rating = 5,
        date_time = gigs[1].date_time_of_request
    )

    gig2_dater = Feedback(
        user = gigs[2].dater.user,
        gig = gigs[2],
        message = 'He was rude, but alright',
        star_rating = 3,
        date_time = gigs[2].date_time_of_request
    )

    gig2_cupid = Feedback(
        user = gigs[2].cupid.user,
        gig = gigs[2],
        message = 'This cupid was great!',
        star_rating = 5,
        date_time = gigs[2].date_time_of_request
    )

    gig0_dater.save()
    gig1_dater.save()
    gig2_cupid.save()
    gig2_dater.save()

def dummy_payment_cards(dater1, dater2, PaymentCard):
    """
    Create sample cards for daters.
    dater1: The first dater
    dater2: The second dater
    PaymentCard: The model to use for PaymentCard
    """

    payment_card1 = PaymentCard(
        user = dater1.user,
        card_number = '09123570987124',
        cvv = '123',
        expiration = '06/26'
    )

    payment_card2 = PaymentCard(
        user = dater2.user,
        card_number = '09100120412404',
        cvv = '138',
        expiration = '04/28'
    )

    payment_card1.save()
    payment_card2.save()

def dummy_bank_accounts(cupid1, cupid2, BankAccount):
    """
    Create sample bank accounts for cupids.
    cupid1: The first cupid
    cupid2: The second cupid
    BankAccount: The model to use for BankAccount
    """
    bank_account1 = BankAccount(
        user = cupid1.user,
        routing_number = '123512512',
        account_number = '13512589798609'
    )

    bank_account2 = BankAccount(
        user = cupid2.user,
        routing_number = '123124987',
        account_number = '13510001248109'
    )

    bank_account1.save()
    bank_account2.save()


def main(apps, schema_editor):
    """
    Call the functions to actually perform the migrations.
    apps: provided by Django, provides access to models
    schema_editor: provided by Django, currently unused
    """
    #Find models
    User = apps.get_model('api', 'User')
    Dater = apps.get_model('api', 'Dater')
    Message = apps.get_model('api', 'Message')
    Gig = apps.get_model('api', 'Gig')
    Quest = apps.get_model('api', 'Quest')
    Cupid = apps.get_model('api', 'Cupid')
    Date = apps.get_model('api', 'Date')
    Feedback = apps.get_model('api', 'Feedback')
    BankAccount = apps.get_model('api', 'BankAccount')
    PaymentCard = apps.get_model('api', 'PaymentCard')

    #Daters
    dater1 = dummy_dater1(User,Dater)
    dater2 = dummy_dater2(User,Dater)
    
    #Cupids
    cupid1 = dummy_cupid1(User,Cupid)
    cupid2 = dummy_cupid2(User,Cupid)

    #Manager
    dummy_manager(User)

    #Messages
    dummy_messages1(dater1.user, Message)
    dummy_messages2(dater2.user, Message)
    
    #Gigs
    gigs = []
    gigs.extend(dummy_unclaimed(dater1, Gig, Quest))
    gigs.extend(dummy_claimed(dater1, cupid1, Gig, Quest))

    #Dates
    dummy_dates(dater1, dater2, Date)

    # Feedback
    dummy_feedbacks(gigs, Feedback)

    #payment cards
    dummy_payment_cards(dater1, dater2, PaymentCard)

    #bank accounts
    dummy_bank_accounts(cupid1, cupid2, BankAccount)

class Migration(migrations.Migration):
    """
    Expected by Django. Makes the migrations happen.
    """


    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(main),
    ]
