package main

import (
	"fmt"
	"os"

	"computorv1/internal/input"
	"computorv1/internal/parse"
)

func computor() error {

	var expression string
	var err error

	if len(os.Args) == 1 {
		expression, err = input.GetExpressionFromStdin()
	} else {
		if len(os.Args) > 1 {
			return fmt.Errorf("Please enter your expression as a single, quoted string")
		}
		expression = os.Args[1]
	}

	fmt.Println(expression)

	err = parse.ParseExpression(expression)

	return err

}

func main() {

	if err := computor(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	os.Exit(0)

}
