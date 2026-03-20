package main

import (
	"encoding/json"
	"os"
)

type Input struct {
	Numbers []int `json:"numbers"`
}

type Output struct {
	Sum int `json:"sum"`
}

func main() {
	var input Input
	if err := json.NewDecoder(os.Stdin).Decode(&input); err != nil {
		os.Exit(1)
	}

	sum := 0
	for _, n := range input.Numbers {
		sum += n * n
	}

	output := Output{Sum: sum}
	if err := json.NewEncoder(os.Stdout).Encode(output); err != nil {
		os.Exit(1)
	}
}
