package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func solve(in *bufio.Reader, out *bufio.Writer) {
	var s string
	Fscan(in, &s)
	ss := []rune(s)
	sets := make(map[rune]bool)
	for _, v := range ss {
		sets[v] = true
	}
	k := len(sets)

	sss := make(map[rune]bool)
	for _, v := range ss[:k] {
		sss[v] = true
	}

	for i := 0; i < len(ss)-k; i++ {
		delete(sss, ss[i])
		sss[ss[i+k]] = true
		if len(sss) != k {
			Fprintln(out, "NO")
			return
		}
	}
	Fprintln(out, "YES")

}

func run(r io.Reader, w io.Writer) {
	in := bufio.NewReader(r)
	out := bufio.NewWriter(w)
	defer out.Flush()
	var a int
	Fscan(in, &a)
	for i := 0; i < a; i++ {
		solve(in, out)
	}

}

func main() {
	run(os.Stdin, os.Stdout)
}
