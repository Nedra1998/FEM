SOURCE = $(shell find -name "*.md")
CHAPTERS = $(SOURCE:%.md=%.pdf)

all: $(CHAPTERS)
	pandoc --template=templates/template.tex -V title="The Mathematical Theoy of Finite Element Methods" -V author="Arden Ramussen" $(SOURCE) -o Master.pdf

%.pdf: %.md
	pandoc --template=templates/template.tex $< -o $@

clean:
	rm Master.pdf $(CHAPTERS)
