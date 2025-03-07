#include <print>
#include <string>
#include <ranges>

using namespace std::literals;


int main() {
	auto x = true;
	if (x) {
		std::println("{}", "Hello, World!"s);
	}
}


