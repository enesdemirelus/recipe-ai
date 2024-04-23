import openai

isUserStillAddingIngredients = True
ingredient = []

while isUserStillAddingIngredients:
    ingredient_from_user = input("Please enter a ingredient (enter q to exit.): ")
    if ingredient_from_user != "q":
        ingredient.append(ingredient_from_user)
    else:
        isUserStillAddingIngredients = False


def recipe_creator(lst):
    openai.api_key = "open ai api key"
    prompt = f"Hi! Can you please provide me a recipe with just this ingredients. Please assume that we have the basic items like water, salt, oil etc. : {lst}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return(response['choices'][0]['message']['content'])



print(recipe_creator(ingredient))


