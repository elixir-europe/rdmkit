# As GitHub Actions are used for GitHub Pages, the branch must be set via environment variable
module Jekyll
  module GitHubMetadata
    class Repository
      def source
        {
          "branch" => ENV["GITHUB_BRANCH"] || "?",
          "path" => ENV["BASE_PATH"] || "/",
        }
      end
    end
  end
end
