#include <print>
#include <string>

using namespace std::literals;


int main() {
	if (false) {
		std::println("{}", 1);
	}
	else if (false) {
		std::println("{}", 2);
	}
	else {
		std::println("{}", 4);
		std::println("{}", 2);
	}
}

