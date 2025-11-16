package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
func solve(p []int64, in *bufio.Reader, out *bufio.Writer) {
	var b int
	Fscan(in, &b)
	L := make([]int64, b)
	var x int64
	for i := 0; i < b; i++ {
		Fscan(in, &x)
		L[i] = x
	}
	for _, v := range p {
		for _, w := range L {
			if gcd(v, w) == 1 {
				Fprintln(out, v)
				return
			}
		}
	}
	Fprintln(out, -1)
	return

}

func run(r io.Reader, w io.Writer) {
	in := bufio.NewReader(r)
	out := bufio.NewWriter(w)
	defer out.Flush()
	var a int
	Fscan(in, &a)
	p := []int64{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53}
	for i := 0; i < a; i++ {
		solve(p, in, out)
	}

}

func main() {
	run(os.Stdin, os.Stdout)
}
