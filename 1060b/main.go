package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func calc(s int) int {
	ans := 0
	for s > 0 {
		ans += s % 10
		s /= 10
	}
	return ans
}

func run(r io.Reader, w io.Writer) {
	in := bufio.NewReader(r)
	out := bufio.NewWriter(w)
	defer out.Flush()
	var a int
	Fscan(in, &a)
	k := 9
	t := 0

	for k < a {
		k *= 10
		k += 9
		t *= 10
		t += 9
	}
	Fprintln(out, calc(a-t)+calc(t))
}

func main() {
	run(os.Stdin, os.Stdout)
}
