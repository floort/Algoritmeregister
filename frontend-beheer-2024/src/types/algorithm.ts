import { FastApiResponse } from '.'
import { Organisation } from './organisation'

export interface Algorithm {
  name?: string
  schema_version?: string
  last_update_dt: string
  lars: string
  source_id?: number
  published: boolean
  current_version_released: boolean
  current_version_published: boolean
  last_update_by: string
  overviewStatus?: string
  last_update_dt_formatted?: string
}

export interface StateChangeAction {
  label: string
  enabled: boolean
  key: string
  origin_state: string
  target_state: string
}

export interface AlgorithmForm {
  name?: string
  organization?: string
  published?: boolean
  create_dt?: Date
  standard_version?: any
  state?: string

  [key: string]: any
}

export interface AlgorithmWithUser extends AlgorithmForm {
  user_id: string
}

export interface AlgorithmListResponse extends FastApiResponse {
  data: Algorithm[]
}

export interface AlgorithmResponse extends FastApiResponse {
  data: AlgorithmForm
}

export interface GetAlgorithmVersionsResponse extends FastApiResponse {
  data: AlgorithmWithUser[]
}

export interface GetAvailableActionsResponse extends FastApiResponse {
  data: StateChangeAction[]
}
export interface CreateAlgorithmResponse extends FastApiResponse {
  data: {
    lars_code: string
  }
}

export interface UpdateAlgorithmResponse extends FastApiResponse {
  data: null | { message: string }
}

export interface RemoveAlgorithmResponse extends FastApiResponse {
  data: null
}

export interface AlgorithmPreviewResponse extends FastApiResponse {
  data: {
    url: string
  }
}

export interface NoOrgResponse extends FastApiResponse {
  data: null
}

export interface AlgorithmOwnerResponse extends FastApiResponse {
  data: Organisation
}

export interface AlgorithmTotalCountResponse extends FastApiResponse {
  data: number
}

export interface ColumnResponse extends FastApiResponse {
  data: {
    column_name: string
    is_nullable: string
  }[]
}

export interface ColumnCountResponse extends FastApiResponse {
  data: {
    count: number
    descriptor: string
  }[]
}

export interface CompletenessResponse extends FastApiResponse {
  data: string
}