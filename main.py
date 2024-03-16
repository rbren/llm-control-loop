from lib.agent import Agent

def main():
    agent = Agent()
    agent.add_thought("I'm thinking about a lot of things.")
    agent.add_thought("My name is Bob.")
    agent.add_thought("I'm hungry.")
    agent.add_thought("I'm tired.")
    agent.add_thought("I'm thinking about a lot of things.")
    docs = agent.memory.search("what's my name?")
    print("docs", docs)
    agent.monologue.condense()
    print(agent.monologue.get_thoughts())

if __name__ == "__main__":
    main()

