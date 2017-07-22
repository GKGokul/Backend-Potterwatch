from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from question_database import Base, Questions

engine = create_engine('sqlite:///quidditch_questions.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

i = 1

Question1 = Questions(index=i, question="Dumbledore's favourite jam flavour?", OptionA="Blueberry", OptionB="Raspberry",
                      OptionC="Strawberry", OptionD="Pineapple", answer="OptionB")
session.add(Question1)
session.commit()

i = i + 1

Question2 = Questions(index=i, question="Who was the last Minister of Magic before Voldemort's death?",
                      OptionA="Armando Dippet", OptionB="Pius Thicknesse", OptionC="Cornelius Fudge",
                      OptionD="Rufus Scrimgeour", answer = "OptionB")
session.add(Question2)
session.commit()

i = i + 1

Question3 = Questions(index=i, question="Which dragon did Victor Krum face in the First Task?",
                      OptionA="Hungarian Horntail", OptionB="Swedish Short Snout", OptionC="Chinese Fireball",
                      OptionD="Common Welsh Green", answer = "OptionC")
session.add(Question3)
session.commit()

i = i + 1

Question4 = Questions(index=i, question="What did Dumbledore leave behind for Hermione after his death?",
                      OptionA="Tales of Beedle the Bard", OptionB="Hogwarts: A History", OptionC="Magical Me",
                      OptionD="The Life and Lies of Albus Dumbledore", answer = "OptionA")
session.add(Question4)
session.commit()

i = i + 1

Question5 = Questions(index=i, question="Which of the following is not an ingredient of the Polyjuice Potion?",
                      OptionA="Boomslang Skin", OptionB="Lacewing Flies", OptionC="Part of a person",
                      OptionD="Acromantula Venom", answer = "OptionD")
session.add(Question5)
session.commit()

i = i + 1

Question6 = Questions(index=i, question="Who among the following is not a Ghost of a Hogwarts House?",
                      OptionA="Sir Nicholas de Mimsy Porpington", OptionB="Bloody Baron", OptionC="Fat Lady",
                      OptionD="Grey Lady", answer = "OptionC")
session.add(Question6)
session.commit()

i = i + 1

Question7 = Questions(index=i, question="What owl grade did Harry initially require to take Potions in his sixth year?",
                      OptionA="Outstanding", OptionB="Exceeds Expectations", OptionC="Troll", OptionD="Acceptable", answer = "OptionA")
session.add(Question7)
session.commit()

i = i + 1

Question8 = Questions(index=i, question="What is the name of the third Weasley child?", OptionA="Bill", OptionB="Percy",
                      OptionC="Charlie", OptionD="Fred", answer = "OptionB")
session.add(Question8)
session.commit()

i = i + 1

Question9 = Questions(index=i, question="Which of the following was not a horcrux?", OptionA="Lost Diadem",
                      OptionB="Resurrection Stone", OptionC="Sword of Gryffindor", OptionD="Nagini", answer = "OptionC")
session.add(Question9)
session.commit()

i = i + 1

Question10 = Questions(index=i, question="Which of the following is not the name of Harry's children?",
                       OptionA="Albus Severus Potter", OptionB="James Sirius Potter", OptionC="Lily Luna Potter",
                       OptionD="Remus Rubeus Potter", answer = "OptionD")
session.add(Question10)
session.commit()
