from markov_python.cc_markov import MarkovChain
import fetch_data

fetch_data.test()


mc = MarkovChain()
mc.add_file('/home/zf/data/winereviews.txt')

mc.add_string("red")

print mc.generate_text(10)
