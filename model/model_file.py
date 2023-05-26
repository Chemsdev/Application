# librairie
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Input, LSTM, Embedding, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.metrics import Mean
import numpy as np
from keras.models import load_model



# =========================================================== Utilitaires ==============================================================>

# chargement du modèle ou du tokenizer.
import pickle
def load(name_file:str):
    file = open(f'model/{name_file}.pkl', 'rb')
    tokenizer_model = pickle.load(file)
    file.close()
    return tokenizer_model

# chargement du modèle & tokenizer
tokenizer = load(name_file="tokenizer_2") 
model     = load_model('model/model.h5', compile=False)

# =====================================================================================================================================>

# Encodage, Décodage.
def encoder_decoder(model):
    latent_dim = 6
    encoder_inputs = model.get_layer('input_6').input
    encoder_lstm = model.get_layer('lstm_2')
    encoder_embedding = model.get_layer('embedding_1')(encoder_inputs)
    encoder_outputs, state_h, state_c = encoder_lstm(encoder_embedding)
    encoder_states = [state_h, state_c]
    decoder_inputs = model.get_layer('input_5').input
    decoder_lstm = model.get_layer('lstm_3')
    decoder_embedding = model.get_layer('embedding_1')(decoder_inputs)
    decoder_outputs, _, _ = decoder_lstm(decoder_embedding, initial_state=encoder_states)
    decoder_dense = model.get_layer('dense_1')
    decoder_outputs = decoder_dense(decoder_outputs)
    encoder_model = Model(encoder_inputs, encoder_states)
    decoder_states_inputs = [Input(shape=(latent_dim,)), Input(shape=(latent_dim,))]
    decoder_outputs, state_h, state_c = decoder_lstm(decoder_embedding, initial_state=decoder_states_inputs)
    decoder_states = [state_h, state_c]
    decoder_outputs = decoder_dense(decoder_outputs)
    decoder_model = Model([decoder_inputs] + decoder_states_inputs, [decoder_outputs] + decoder_states)
    return decoder_model, encoder_model

# ===================================================================================================================================>


# Fonction permettent de préparer la data.
def preprocess_data(features:list, tokenizer):
    input_sequence = ' '.join(features)
    input_sequence_sequence = tokenizer.texts_to_sequences([input_sequence])
    input_sequence_padded = pad_sequences(np.array(input_sequence_sequence), maxlen=2785, padding='post')
    return input_sequence_padded

# ===================================================================================================================================>

# Génération texte.
def generate_text(input_sequence, encoder_model, decoder_model, tokenizer):
    states_value = encoder_model.predict(input_sequence)
    target_sequence = np.zeros((1, 1))  # Start with empty target sequence
    stop_condition = False
    generated_text = []
    while not stop_condition:
        output_tokens, h, c = decoder_model.predict([target_sequence] + states_value)
        sampled_token_index = np.argmax(output_tokens[0, -1, :])

        # Check if the sampled token index exists in the vocabulary
        if sampled_token_index in tokenizer.index_word:
            sampled_word = tokenizer.index_word[sampled_token_index]
            generated_text.append(sampled_word)
            print(np.max(output_tokens))
        else:
            # Handle the case when the token index is not found
            remaining_indices = set(range(len(tokenizer.index_word))) - {0}  # Exclude the unknown token
            if len(remaining_indices) > 0:
                sampled_token_index = np.random.choice(list(remaining_indices))
                sampled_word = tokenizer.index_word[sampled_token_index]
                generated_text.append(sampled_word)
                print(np.max(output_tokens))
            else:
                # Handle the case when no valid token indices are available
                sampled_word = '<unknown>'
                generated_text.append(sampled_word)
                print('No valid token indices available.')

        # Update the stop condition based on the generated token
        if sampled_word == '<end>' or len(generated_text) > 100:
            stop_condition = True

        target_sequence = np.array([[sampled_token_index]])  # Update the target sequence
        states_value = [h, c]

    return ' '.join(generated_text)

# ===================================================================================================================================>

def modeling(features:list, model=model, tokenizer=tokenizer):
    
    # étape 1
    decoder_model, encoder_model = encoder_decoder(model)
    
    # étape 2
    input_sequence_padded = preprocess_data(
        features=features,
        tokenizer=tokenizer
    )
    
    # étape 3
    generated_text = generate_text(
                        input_sequence=input_sequence_padded, 
                        encoder_model=encoder_model, 
                        decoder_model=decoder_model,
                        tokenizer=tokenizer
                    )
    
    # On retourne la prédiction.
    return generated_text



