from lib.monologue import Monologue

def main():
    monologue = Monologue()
    monologue.add_thought("I'm thinking about a lot of things.")
    monologue.add_thought("My name is Bob.")
    monologue.add_thought("I'm hungry.")
    monologue.add_thought("I'm tired.")
    monologue.add_thought("I'm thinking about a lot of things.")
    monologue.condense()
    print(monologue.get_thoughts())

if __name__ == "__main__":
    main()

