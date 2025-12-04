package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
func solve(a int, in *bufio.Reader, out *bufio.Writer) {

}

func run(x io.Reader, w io.Writer) {
	in := bufio.NewReader(x)
	out := bufio.NewWriter(w)
	defer out.Flush()
	var a int
	Fscan(in, &a)
	var l, r int
	L := make([][]int, a)
	for i := 0; i < a; i++ {

		L[i] = make([]int, 2)
		Fscan(in, &L[i][0], &L[i][1])
		l += L[i][0]
		r += L[i][1]
	}
	num := 0
	ans := abs(l - r)
	for i := 0; i < a; i++ {
		k := abs(l - r - L[i][0]*2 + 2*L[i][1])
		if ans < k {
			num = i + 1
			ans = k
		}
	}
	Fprintln(out, num)

}

func main() {
	run(os.Stdin, os.Stdout)
}
