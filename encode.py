from sys import *
if len(argv) > 1:
	string = open(argv[1], "r").read();
else:
	string = "Hello, World!";

# Huffman Tree Classes/Objects
class Tree:
	type = "tree";

	lb = None; # Can Be Another Tree Or Leaf
	rb = None; # Can Be Another Tree Or Leaf

	val = 0;

	def __init__(self, lb, rb):
		self.lb = lb;
		self.rb = rb;

		self.val = lb.val + rb.val;

	def getTree(self):
		# print("[", self.lb.type, ",", self.rb.type,"]");
		return str("Branch[{}]:[Left:" + self.lb.getTree() + ",Right:" + self.rb.getTree() + "]").format(self.val);

class Leaf:
	type = "leaf";

	char = None;
	val  = None;

	def __init__(self, char, val):
		self.char = char;
		self.val = val;

	def getTree(self):
		return str("Leaf:[{}, {}]".format(self.char, self.val));



def main(input):
	print("Input String:", input);
	# Sort All Chars Into Order Of Least-Most Used
	freq = { };
	for char in input:
		try:
			# Add 1 to freq list
			freq[char] += 1;
		except (KeyError):
			# Create Char In Freq List If Dosent Exist
			freq[char] = 1;

	# Sort Dictionary
	sorted_freq = dict(sorted(freq.items(), key=lambda kv: kv[1]));
	print(sorted_freq);

	# Convert To Array (To Loop Easier :p)
	treeArr = [];
	for key in sorted_freq:
		treeArr.append(Leaf(key, sorted_freq[key]));

	# Build Tree
	while len(treeArr) > 1:
		print("Creating Tree:", treeArr[0].type, "&&", treeArr[1].type);
		tree = Tree(treeArr[0], treeArr[1]);
		treeArr.remove(treeArr[0]); treeArr.remove(treeArr[0]);

		# Insert Tree To treeArr
		inserted = False;
		for i in range(0, len(treeArr)):
			if (tree.val < treeArr[i].val):
				treeArr.insert(i, tree);
				inserted = True;
				break;
		# If not Inserted, append to end
		if inserted == False:
			treeArr.append(tree);

	print(treeArr[0].getTree());

main(string);