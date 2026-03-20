package main
import "testing"
func TestCalculateLogic(t *testing.T) {
	if calculateLogic([]int{1,2,3}) != 14 {
		t.Fail()
	}
}
