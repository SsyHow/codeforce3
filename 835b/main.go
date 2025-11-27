package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"slices"
)

func solve(in *bufio.Reader, out *bufio.Writer) {
	var b int
	Fscan(in, &b)
}

func run(r io.Reader, w io.Writer) {
	in := bufio.NewReader(r)
	out := bufio.NewWriter(w)
	defer out.Flush()
	var k int
	var n string

	Fscan(in, &k, &n)

	d := make([]rune, 0)
	cur := 0
	for _, v := range n {
		d = append(d, rune(v)-'0')
		cur += int(rune(v) - '0')
	}
	slices.Sort(d)
	ans := 0
	for _, v := range d {
		if cur < k {
			cur += 9 - int(v)
			ans += 1
		}
	}
	Fprintln(out, ans)
}

func main() {
	run(os.Stdin, os.Stdout)
}
