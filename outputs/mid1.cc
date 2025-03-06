#include <print>
#include <string>

using namespace std::literals;


int main() {
	auto x = true;
	if (x) {
		std::println("{}", "Hello, World!"s);
	}
}

