#include <print>
#include <string>
#include <vector>
#include <ranges>

using namespace std::literals;


int main()
{
	auto x = std::vector{"a"s, "b"s, "c"s, "x"s, "y"s, "z"s};
	for (const auto& elt : x) {
		std::println("{}", elt);
		if (elt == "x"s) break;
	}
	std::println("{}", "done!"s);
}


