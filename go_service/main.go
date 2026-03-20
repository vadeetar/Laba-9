package main

import (
	"encoding/json"
	"log"
	"net/http"
)

type Input struct {
	Numbers []int `json:"numbers"`
}

type Output struct {
	Result int `json:"result"`
}

func calculateLogic(numbers []int) int {
	sum := 0
	for _, n := range numbers {
		sum += n * n
	}
	return sum
}

func calculate(w http.ResponseWriter, r *http.Request) {
	var input Input
	if err := json.NewDecoder(r.Body).Decode(&input); err != nil {
		http.Error(w, "invalid JSON", http.StatusBadRequest)
		return
	}
	result := calculateLogic(input.Numbers)
	json.NewEncoder(w).Encode(Output{Result: result})
}

func main() {
	http.HandleFunc("/calculate", calculate)
	log.Fatal(http.ListenAndServe(":8080", nil))
}
