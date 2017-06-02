from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User
from project.db.database_connect import connect_to_database


def db_seed():
    """Seed the db so it isn't empty at start"""
    session = connect_to_database()
    # Create dummy user
    User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
                picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
    session.add(User1)
    session.commit()

    # Item for Tennis
    category1 = Category(user_id=1, name="Tennis", description="Come here for all of your tennis needs. We have everything from raquests to tickets to Wimbledon.")

    session.add(category1)
    session.commit()

    item1 = Item(user_id=1, name="Tennis balls", description="Nice, fresh green tennis balls guaranteed to last.",
                        price="$2.99", category=category1)

    session.add(item1)
    session.commit()

    item2 = Item(user_id=1, name="Wilson Pro Staff RF97", description="Helped designed by the great Roger Federer himself.",
                        price="$159.00", category=category1)

    session.add(item2)
    session.commit()

    item3 = Item(user_id=1, name="Grip", description="You'll regret not having grip.",
                        price="$3.99", category=category1)

    session.add(item3)
    session.commit()

    item4 = Item(user_id=1, name="String", description="If it breaks within the first week, we'll replace it for free.",
                        price="$19.99", category=category1)

    session.add(item4)
    session.commit()

    item5 = Item(user_id=1, name="Towels", description="You'll regret not having one when the humidity high.",
                        price="$5.99", category=category1)

    session.add(item5)
    session.commit()

    item6 = Item(user_id=1, name="Sunscreen", description="So strong you'll glow in the sun.",
                        price="$.99", category=category1)

    session.add(item6)
    session.commit()


    # Item for Baseball
    category2 = Category(user_id=1, name="Baseball", description="Baseball goods for all ages")

    session.add(category2)
    session.commit()


    item1 = Item(user_id=1, name="Pair of Gloves", description="The perfect combination to play catch with your child.",
                        price="$19.99", category=category2)

    session.add(item1)
    session.commit()

    item2 = Item(user_id=1, name="10 Balls",
                        description="Puts the ball in baseball", price="$9.99", category=category2)

    session.add(item2)
    session.commit()

    item3 = Item(user_id=1, name="Babe Ruth t-shirt", description="Worn by the great Babe Ruth himself in his very last game.",
                        price="$1999.99", category=category2)

    session.add(item3)
    session.commit()

    item4 = Item(user_id=1, name="Eastoon Mako Youth Bat", description="If you don't hit a homerun with this, we'll give you your money back.",
                        price="$179.99", category=category2)

    session.add(item4)
    session.commit()


    # Item for Basketball
    category1 = Category(user_id=1, name="Basketball", description="Arguably the best sport in the entire universe")

    session.add(category1)
    session.commit()


    item1 = Item(user_id=1, name="MJ Jersey", description="If you play basketball, then you know the great Michael Jordan. This jersey was made by the man himself (source needed)",
                        price="$1.99", category=category1)

    session.add(item1)
    session.commit()

    item2 = Item(user_id=1, name="Wilson Evolution Ball", description="In order to play great, you need a great ball.",
                        price="$20.99", category=category1)

    session.add(item2)
    session.commit()

    item3 = Item(user_id=1, name="Stell-framed Portable Hooop", description="Who needs to go to a court when you can buy this and play in your own backyard.",
                        price="$199.95", category=category1)

    session.add(item3)
    session.commit()

    item4 = Item(user_id=1, name="Net", description="Nothing like hearing the net go *swish*.",
                        price="$5.99", category=category1)

    session.add(item4)
    session.commit()

    item2 = Item(user_id=1, name="Shoes", description="Have you ever played basketball without shoes? Try it, then come back and buy this after you hurt yourself.",
                        price="$79.50", category=category1)

    session.add(item2)
    session.commit()

    print "added items!"
