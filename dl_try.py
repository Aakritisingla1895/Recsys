from keras.layers import Input, Embedding, Dot, Reshape, Dense
from keras.models import Model

def book_embedding_model(embedding_size = 50, classification = False):
    """Model to embed books and wikilinks using the Keras functional API.
       Trained to discern if a link is present in on a book's page"""
    
    # Both inputs are 1-dimensional
    book = Input(name = 'book', shape = [1])
    link = Input(name = 'link', shape = [1])
    
    # Embedding the book (shape will be (None, 1, 50))
    book_embedding = Embedding(name = 'book_embedding',
                               input_dim = len(book_index),
                               output_dim = embedding_size)(book)
    
    # Embedding the link (shape will be (None, 1, 50))
    link_embedding = Embedding(name = 'link_embedding',
                               input_dim = len(link_index),
                               output_dim = embedding_size)(link)
    
    # Merge the layers with a dot product along the second axis 
    # (shape will be (None, 1, 1))
    merged = Dot(name = 'dot_product', normalize = True, 
                 axes = 2)([book_embedding, link_embedding])
    
    # Reshape to be a single number (shape will be (None, 1))
    merged = Reshape(target_shape = [1])(merged)
    
    # Squash outputs for classification
    out = Dense(1, activation = 'sigmoid')(merged)
    model = Model(inputs = [book, link], outputs = out)
    
    # Compile using specified optimizer and loss 
    model.compile(optimizer = 'Adam', loss = 'binary_crossentropy', 
                  metrics = ['accuracy'])
    
    return model