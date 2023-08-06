from graphviz import Digraph

def gen_sample():
    dot = Digraph('sample', 
                node_attr={'color': 'lightblue2', 'style': 'filled'})
    dot.format = 'svg'
    #dot.attr(rankdir='LR', size = "24,32")
    dot.graph_attr.update(rankdir='LR', size = "24,32")
    dot.node('s3_data_source')
    dot.node('raw_data.tar.gz')
    dot.node('preprocessed_data')
    dot.node('feature_1')
    dot.node('feature_2')
    dot.node('model_initial')
    dot.node('model_final')

    dot.edge('s3_data_source', 'raw_data.tar.gz', label = 'download_data.py')
    dot.edge('raw_data.tar.gz', 'preprocessed_data', label='preprocess_data.py')
    dot.edge('preprocessed_data', 'feature_1', label = 'pca_transform.py')
    dot.edge('preprocessed_data', 'feature_2', label = 'svd_transform.py')
    dot.edge('feature_1', 'model_initial', label='model_initial.py')
    dot.edge('feature_2', 'model_initial', label='model_initial.py')
    dot.edge('model_initial', 'model_final', label='model_final.py')
    dot.render('sample')

def gen_step_1():
    dot = Digraph('step_1', 
                node_attr={'color': 'lightblue2', 'style': 'filled'})
    dot.format = 'svg'
    dot.graph_attr.update(rankdir='LR', size = "24,32")
    dot.node('gen_raw_1.py')
    dot.node('raw_data_1.txt')
    dot.edge('gen_raw_1.py', 'raw_data_1.txt', label='python gen_raw_1.py > raw_data_1.txt')
    dot.render('step_1')

def gen_step_2():
    dot = Digraph('step_2', 
                node_attr={'color': 'lightblue2', 'style': 'filled'})
    dot.format = 'svg'
    dot.graph_attr.update(rankdir='LR', size = "24,32")
    dot.node('gen_raw_1.py')
    dot.node('raw_data_1.txt')
    dot.edge('gen_raw_1.py', 'raw_data_1.txt', label='python gen_raw_1.py > raw_data_1.txt')
    dot.node('processed.txt')
    dot.node('gen_processed.py')
    dot.edge('raw_data_1.txt', 'processed.txt', label='python gen_processed.py')
    dot.edge('gen_processed.py', 'processed.txt', label='python gen_processed.py')

    
    dot.render('step_2')


if __name__ == '__main__':
    #gen_sample()
    #gen_step_1()
    gen_step_2()