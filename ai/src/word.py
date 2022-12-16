class Word:
    def __init__(self, quantity, emotion, priority, nature, pronouns, pos_x,
                 pos_y, pos_z, family, context):
        self.quantity = quantity
        self.emotion = emotion
        self.priority = priority
        self.nature = nature
        self.pronouns = pronouns
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z
        self.family = family
        self.context = context

    def content(self):
        word_matrix = {
            "qty": self.quantity,
            "emotion": self.emotion,
            "priority": self.priority,
            "nature": self.nature,
            "pronouns": self.pronouns,
            "pos_x": self.pos_x,
            "pos_y": self.pos_y,
            "pos_z": self.pos_z,
            "family": self.family,
            "context": self.context
        }

        return word_matrix


# import tensorflow as tf
# import numpy as np
#
# # Load the training data
# data = []
# with open("data.txt") as f:
#     for line in f:
#         data.append(line.strip())
#
# # Preprocess the data
# def preprocess(data):
#     # Tokenize the words
#     tokenizer = tf.keras.preprocessing.text.Tokenizer(filters='')
#     tokenizer.fit_on_texts(data)
#     sequences = tokenizer.texts_to_sequences(data)
#
#     # Pad the sequences to the same length
#     max_length = max([len(seq) for seq in sequences])
#     sequences = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=max_length, padding="post")
#
#     # Create a vocabulary of words
#     vocab_size = len(tokenizer.word_index) + 1
#     return sequences, vocab_size, tokenizer
#
# sequences, vocab_size, tokenizer = preprocess(data)
#
# # Split the data into training and test sets
# train_data = sequences[:int(len(sequences) * 0.8)]
# test_data = sequences[int(len(sequences) * 0.8):]
#
# # Define the model
# model = tf.keras.Sequential()
# model.add(tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=64, input_length=max_length))
# model.add(tf.keras.layers.LSTM(64))
# model.add(tf.keras.layers.Dense(vocab_size, activation="softmax"))
#
# # Compile the model
# model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
#
# # Train the model
# model.fit(train_data, epochs=10, validation_data=test_data)
#
# # Save the model
# model.save("chatbot_model.h5")
#
# # Load the model
# model = tf.keras.models.load_model("chatbot_model.h5")
#
# # Define a function to generate responses
# def generate_response(prompt, model, tokenizer):
#     # Tokenize the prompt
#     prompt_tokens = tokenizer.texts_to_sequences([prompt])
#     prompt_tokens = tf.keras.preprocessing.sequence.pad_sequences(prompt_tokens, maxlen=max_length, padding="post")
#
#     # Generate a response
#     response = model.predict(prompt_tokens)[0]
#     response = np.argmax(response)
#
#     # Convert the response back to a word
#     for word, index in tokenizer.word_index.items():
#         if index == response:
#             return word
#
# # Test the chatbot
# while True:
#     prompt = input("You: ")
#     response = generate_response(prompt, model, tokenizer)
#     print("Bot:", response)
