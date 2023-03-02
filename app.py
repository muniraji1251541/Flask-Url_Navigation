from flask import Flask,render_template

AI=Flask(__name__)

@AI.route('/firstpage')
def first():
	return render_template('first.html')

@AI.route('/secondpage')
def second():
	return render_template('second.html')


if __name__=='__main__':
	AI.run(debug=True)