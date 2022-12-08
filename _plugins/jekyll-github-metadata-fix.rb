# As GitHub Actions are used for GitHub Pages, the branch must be set via environment variable
module Jekyll
    module GitHubMetadata
        module RepositoryFix
            def source
                {
                    "branch" => ENV["GITHUB_BRANCH"] || super["branch"],
                    "path" => ENV["BASE_PATH"] || super["path"],
                }
            end
        end
        class Repository
            prepend RepositoryFix
        end
    end
end
