# frozen_string_literal: true

describe pip('awscli') do
  it { should be_installed }
end
