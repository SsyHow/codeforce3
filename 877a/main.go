package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"strings"
)

func solve(in *bufio.Reader, out *bufio.Writer) {
	var b int
	Fscan(in, &b)
}

func run(r io.Reader, w io.Writer) {
	in := bufio.NewReader(r)
	out := bufio.NewWriter(w)
	defer out.Flush()
	var s string
	Fscan(in, &s)
	ans := 0
	for strings.Contains(s, "Danil") {
		ans += 1
		s = strings.Replace(s, "Danil", "_", 1)
	}
	for strings.Contains(s, "Olya") {
		ans += 1
		s = strings.Replace(s, "Olya", "_", 1)
	}
	for strings.Contains(s, "Slava") {
		ans += 1
		s = strings.Replace(s, "Slava", "_", 1)
	}
	for strings.Contains(s, "Ann") {
		ans += 1
		s = strings.Replace(s, "Ann", "_", 1)
	}
	for strings.Contains(s, "Nikita") {
		ans += 1
		s = strings.Replace(s, "Nikita", "_", 1)
	}
	if ans == 1 {
		Fprintln(out, "YES")
	} else {
		Fprintln(out, "NO")
	}
}

func main() {
	run(os.Stdin, os.Stdout)
}
