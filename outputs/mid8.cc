#include <print>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <tuple>
#include <ranges>

using namespace std::literals;





int main()
{
	auto v = std::vector{"Hey!"s, "Name is"s, "aliiii"s};
	for (const auto& e : v) std::println("{}", e);
}


