#include <print>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <tuple>
#include <ranges>

using namespace std::literals;


auto func() {
}

auto a() {
	if (true) {
	}
	else 
	;	// "pass". Separate line to silence warning.
}

auto b() {
	if (true) {
		if (false) {
			if (1) {
			}
			else 
			;	// "pass". Separate line to silence warning.
		}
		else 
		;	// "pass". Separate line to silence warning.
	}
	else 
	;	// "pass". Separate line to silence warning.
}

auto c() {
	if (true) {
		if (false) {
			if (1) {
			}
			else {
				1;
				2;
			}
		}
		else {
			3;
			4;
		}
	}
	else {
		5;
		6;
	}
}
int main()
{
}


