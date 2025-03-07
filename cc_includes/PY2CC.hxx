// #include <vector>



// template <typename T> // has to be a template anyway
// class std::formatter<std::vector<T>> {
// public:
// 	constexpr auto parse(const auto& ctx) const noexcept { return ctx.begin(); }

// 	auto format(const std::vector<T>& v, auto& ctx) const {
// 		auto out = std::format_to(ctx.out(), "[");

// 		const size_t size = v.size();
//         for (size_t i = 0; i < size; ++i) {
//             out = std::format_to(out, "{}", v[i]);

//             if (i < size - 1)
// 				out = std::format_to(out, ", ");
//         }

//         return std::format_to(out, "]");
// 	}
// };

