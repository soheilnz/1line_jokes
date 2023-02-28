import pyjokes

joke = pyjokes.get_joke(language="en", category="all")
print(joke)

jokes = pyjokes.get_jokes("en", "neutral")
for i in range(5):
    print(jokes[i], "\n")
