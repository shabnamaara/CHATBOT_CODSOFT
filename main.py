import re
import random
class RuleBot:
  ### Potential Negative Response
  negative_responses=("no","nope","nah","naw","not a chance","sorry")
  ### Exit conversation keywords
  exit_commands=("quit","pause","exit","goodbye","bye","later")
  ###Random starter question
  random_questions=(
      "Why are you here?",
      "Are there many humans like you",
      "What do you consume for sustenance?",
      "Is there intelligent life on this planet?",
      "Dose Earth have a leader?",
      "what planets have you visited?",
      "what technology do you have on this planet?"
  )
  def __init__(self):
    self.alienbabble={'describe_planet_intent':r'.*\s*your planet.*',
                       'answer_why_intent':r'why\sare.*',
                       'about_intellipat':r'.*\s*intellipaat',
                       'about_session':r'.*\s*session'
                       }
  def greet(self):
    self.name=input("what is your name?\n")
    will_help=input(
        f"Hi{self.name},I am Rule-Bot.Will you help me learn about your planet?\n")
    if will_help in self.negative_responses:
          print("ok,have a nice earth day!")
          return
    self.chat()

  def make_exit(self,reply):
    for command in self.exit_commands:
      if reply == command:
        print("okay,have a nice earth day!")
        return True

  def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
          reply=input(self.match_reply(reply))

  def match_reply(self,reply):
    for key,value in self.alienbabble.items():
      intent=key
      regex_pattern=value
      found_match=re.match(regex_pattern,reply)
      if found_match and intent == 'describe_planet_intent':
        return self.describe_planet_intent()
      elif found_match and intent =='about_why_intellipat':
         return self.answer_why_intent()
      elif found_match and intent =='about_intellipat':
         return self.about_intellipat()
      elif found_match and intent =='about_session':
         return self.about_session()
    if not found_match:
      return self.no_match_intent()

  def describe_planet_intent(self):
    responses=("My planet is a utopia of diverse organism and species.\n",
              "I am from Opidipus,the capital of the wayward galaxies.\n")
    return random.choice(responses)

  def answer_why_intent(self):
     responses=("I came in peace\n","I am here to collect data on your planet and its inhabitants\n",
              "I heard the coffee is good\n")
     return random.choice(responses)

  def about_intellipaat(self):
     responses=("Intellipaat is world's largest professional educational company\n","Intellipaat will make you learn concepts in the way never\n",
              "Intellipaat is where your career and skill grows\n")
     return "Intellipaat is great place to learn\n"

  def about_session(self):
     responses=("session is on 12th may\n",'session was cool!')
     return random.choice(responses)

  def no_match_intent(self):
    responses=(
        "Please tell me more.\n","Tell me more!\n","why do you say that?\n","I see. Can you elaborate?\n",
        "Interesting.Can you tell me more?\n","I see.How do you think?\n","why?\n",
        "How do you think i feel when you say that?\n")
    return random.choice(responses)

AlienBot=RuleBot()
AlienBot.greet()